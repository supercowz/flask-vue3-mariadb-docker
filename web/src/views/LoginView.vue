<template>
  <div class="row">
    <div class="one-half column offset-by-three">
      <form @submit.prevent="login">
        <h4>Login</h4>
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" class="u-full-width" required>
        
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" class="u-full-width" required>
        
        <button type="submit" class="button-primary u-full-width">Login</button>
      </form>
      <p>Don't have an account? <router-link to="/register">Register</router-link></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const router = useRouter();

const login = async () => {
  const success = await useAuthStore().login(username.value, password.value);

  username.value = '';
  password.value = '';
  if (!success) {
    alert('Login failed');
    return;
  }
  else {
    router.push({ name: 'home' });
  }
};
</script>

<style scoped>
</style>
