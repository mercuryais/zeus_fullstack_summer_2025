console.log('JS Loop DOM Usage');

const mainElement = document.getElementsByTagName('main');

console.log(mainElement);

const ulElement = document.createElement('ul');

const liElOne = document.createElement('li');
liElOne.textContent = 'Bauzu';

const liElTwo = document.createElement('li');
liElTwo.textContent = 'Naashaa Tsaashaa';

const liElThree = document.createElement('li');
liElThree.textContent = 'Sichuan Roasted Beef';

ulElement.appendChild(liElOne);
ulElement.appendChild(liElTwo);
ulElement.appendChild(liElThree);

const main = mainElement[0];

main.appendChild(ulElement);


const sectionElement = document.getElementsByTagName('section');
console.log(sectionElement);

const section = sectionElement[0];
const aOne = document.createElement('a');
const aTwo = document.createElement('a');
const aThree = document.createElement('a');

aOne.setAttribute('href', 'https://www.facebook.com/');
aOne.textContent = 'Facebook';
aTwo.setAttribute('href', 'https://www.instagram.com/');
aTwo.textContent = 'Instagram';
aThree.setAttribute('href', 'https://www.youtube.com/');
aThree.textContent = 'Youtube';


const h1Tag = document.createElement('h1');
h1Tag.textContent = 'My favourite movies.';
section.appendChild(h1Tag);
section.appendChild(aOne);
section.appendChild(aTwo);
section.appendChild(aThree);

const mongolianNationalSports = ['Wrestling', 'Archery', 'Horse Racing'];

const nationalSportsSection = document.createElement('section');

const nationalListUl = document.createElement('ul');
nationalSportsSection.appendChild(nationalListUl);

for (let i = 0; i < mongolianNationalSports.length; i++) {
    const liElement = document.createElement('li');
    liElement.textContent = mongolianNationalSports[i];
    nationalListUl.appendChild(liElement)
}
main.appendChild(nationalSportsSection)