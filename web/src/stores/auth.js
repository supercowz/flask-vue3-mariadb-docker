import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    loggedIn: ref(localStorage.getItem('token') !== null)
  }),
  actions: {
    async login(username, password) {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "username": username, "password": password })
      });

      if (response.ok) {
        const json_data = await response.json();
        localStorage.setItem('token', json_data['access_token']);
        this.loggedIn = true;
        return true;
      }
      return false;
    },
    async register(username, password) {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "username": username, "password": password })
      });

      if (response.ok) {
        return true;
      }
      return false;
    },
    async logout() {
      localStorage.removeItem('token');
      this.loggedIn = false;
      return true;
    }
  }
});
