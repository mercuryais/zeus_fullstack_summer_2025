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
        main: "./static_src/ts/main.ts",
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
