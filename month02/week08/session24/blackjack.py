import sqlite3
import random 
import os
import time

# DB_FILE = # TODO
def get_db_connection():
    conn.row_factory = sqlite3.Row
    return conn
def setup_database():
    """`players` хүснэгт байхгүй бол үүсгэнэ."""
    conn = get_db_connection()
    conn.commit()
    conn.close()
def get_or_create_player(name, starting_chips=1000):
    if player_data:
        print(f"Эргэн тавтай морил, {name}!")
        chips = player_data['chips']
    else:
        print(f"Шинэ тоглогч {name}, тавтай морилно уу!")
        conn.commit()
        chips = starting_chips
    conn.close()
    return chips
def update_chips(name, chips):
    conn.commit()
    conn.close()
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
    'A']
    suits = ['♠', '♥', '♦', '♣']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in
    suits]
    random.shuffle(deck)
    return deck
def get_card_value(card):
    rank = card['rank']
    if rank in ['J', 'Q', 'K']:
        return 10
    if rank == 'A':
        return 11
    return int(rank)
def calculate_hand_value(hand):
    """Гарт байгаа хөзрүүдийн нийлбэр оноог тооцоолно (A-г зөв
    тооцоолно)."""
    value = sum(get_card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'A')
    # Хэрэв нийлбэр 21-ээс хэтэрсэн бол A-г 1 гэж тооцно
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value
def display_cards(player_hand, dealer_hand, hide_dealer_card=False):

    clear_screen()
    player_cards = " ".join([f"[{card['rank']}{card['suit']}]" for card in
    player_hand])
    player_value = calculate_hand_value(player_hand)
    print(f"Таны мод ({player_value}): {player_cards}")
    if hide_dealer_card:
        dealer_cards = f"[{dealer_hand[0]['rank']}{dealer_hand[0]
        ['suit']}] [?]"
        print(f"Дилерийн мод: {dealer_cards}")
    else:
        dealer_cards = " ".join([f"[{card['rank']}{card['suit']}]" for
        card in dealer_hand])
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Дилерийн мод ({dealer_value}): {dealer_cards}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bet(max_bet):
    while True:
        try:
            bet = int(input(f"Бооцоогоо тавина уу (1 - {max_bet}): "))
            if 1 <= bet <= max_bet:
                return bet
            else:
                print("Бооцооны дүн буруу байна. Дахин оролдоно уу.")
        except ValueError:
            print("Зөвхөн тоо оруулна уу.")
def play_game():
    setup_database()
    clear_screen()
    print("♠ ♥ ♦ ♣ Python SQLite Blackjack тоглоомд тавтай морилно уу! ♣ ♦ ♥ ♠")
    player_name = input("Нэрээ оруулна уу: ").strip()
    if not player_name:
        print("Тоглохын тулд нэр оруулах шаардлагатай. Гарч байна.")
        return
    chips = get_or_create_player(player_name)
    while True:
        if chips <= 0:
            print("Таны чипс дууслаа! Дараа дахин мөнгөтэй болоод ирээрэй. 😉 ")
            break
        print(f"\nТаны одоогийн үлдэгдэл: {chips} чипс")
        bet = get_bet(chips)
        chips -= bet
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        player_turn = True
        while player_turn:
            display_cards(player_hand, dealer_hand, hide_dealer_card=True)
            print(f"\nТаны бооцоо: {bet} чипс")
            player_value = calculate_hand_value(player_hand)
            if player_value == 21:
                print("Блэкжэк! Та яллаа!")
                player_turn = False
                continue
            action = input("(Д)ахиад авах уу, (З)огсох уу? ").lower()
            if action.startswith('д'):
                player_hand.append(deck.pop())
                if calculate_hand_value(player_hand) > 21:
                    display_cards(player_hand, dealer_hand, hide_dealer_card=True)
                    print("\nХэтэрлээ! Та энэ удаа ялагдлаа.")
                    player_turn = False
            elif action.startswith('з'):
                player_turn = False
            else:
                print("Буруу үйлдэл. 'Д' эсвэл 'З' үсгийг оруулна уу.")
                time.sleep(1)
        player_value = calculate_hand_value(player_hand)
        if player_value <= 21:
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                display_cards(player_hand, dealer_hand)
                time.sleep(1)
        display_cards(player_hand, dealer_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        print("\n--- Үр Дүн ---")
        if player_value > 21:
            print(f"Та хэтрүүлсэн тул {bet} чипс алдлаа.")
        elif dealer_value > 21:
            print(f"Дилер хэтрүүллээ! Та {bet} чипс хожлоо!")
            chips += bet * 2
        elif player_value == 21 and len(player_hand) == 2:
            print(f"Блэкжэк! Та {int(bet * 1.5)} чипс хожлоо!")
            chips += bet + int(bet * 1.5)
        elif player_value > dealer_value:
            print(f"Та {bet} чипс хожлоо!")
            chips += bet * 2
        elif player_value < dealer_value:
            print(f"Дилер яллаа. Та {bet} чипс алдлаа.")
        else:
            print("Тэнцлээ! Таны бооцоо буцаалаа.")
            chips += bet
        update_chips(player_name, chips)
        print(f"Таны шинэ үлдэгдэл: {chips} чипс")
        
        play_again = input("\nДахин тоглох уу? (Т/Ү) ").lower()
        if not play_again.startswith('т'):
            break
        print("Тоглосонд баярлалаа!")


if __name__ == "__main__":
    play_game()