import path from 'path'
import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react-swc'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(), 
    tailwindcss()
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  define: {
    // Make environment variables available to the frontend
    __API_URL__: JSON.stringify(process.env.VITE_API_URL || '/api'),
  },
  server: {
    proxy: {
      '/api': {
        target: process.env.VITE_API_TARGET || 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
        // Remove /api prefix when forwarding to backend
        rewrite: (path) => path.replace(/^\/api/, ''),
      }
    }
  }
})
