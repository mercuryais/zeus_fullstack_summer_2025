import { defineConfig } from "vite";
export default defineConfig({
  build: {
    // Хөрвүүлсэн файлын гаралтын хавтас
    outDir: "./static/dist",
    emptyOutDir: true,
    manifest: false,
    rollupOptions: {
      input: {
        // Манай TypeScript эх кодны байршил
        pokemon: "./static_src/ts/pokemon.ts",
      },
      output: {
        // Файлын нэрийг хэшлэхгүй, 'main.js' гэж гаргана
        entryFileNames: `[name].js`,
        chunkFileNames: `[name].js`,
        assetFileNames: `[name].[ext]`,
      },
    },
  },
});
