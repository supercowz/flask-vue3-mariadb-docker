<template>
  <div class="row">
    <div class="one-half column offset-by-three">
      <form @submit.prevent="register">
        <h4>Register</h4>
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" class="u-full-width" required>
        
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" class="u-full-width" required>

        <label for="confirmPassword">Confirm Password</label>
        <input type="password" id="confirmPassword" class="u-full-width" v-model="confirmPassword" required>
        
        <button type="submit" class="button-primary u-full-width">Register</button>
      </form>
      <p>Already have an account? <router-link to="/login">Login</router-link></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const confirmPassword = ref('');
const router = useRouter();

const register = async () => {
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match');
    return;
  }

  const success = await useAuthStore().register(username.value, password.value);

  if (!success) {
    alert('Registration failed');
    password.value = '';
    confirmPassword.value = '';
    return;
  }
  else {
    username.value = '';
    password.value = '';
    confirmPassword.value = '';
    alert('Registration successful. Please log in.');
    router.push({ name: 'login' });
  }
};

</script>

<style scoped>
</style>
