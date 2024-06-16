<template>
  <header>
    <div class="wrapper">
      <nav class="nav-primary">
        <RouterLink to="/" class="brand-logo">MySite</RouterLink>
        <ul v-if="isLoggedIn">
          <li @click="logout">Logout</li>
        </ul>
      </nav>
    </div>
  </header>

  <div class="container">
    <RouterView />
  </div>
</template>

<script setup>
import { useAuthStore } from './stores/auth';
import { useRouter } from 'vue-router';
import { onMounted, ref, watchEffect } from 'vue';

const authStore = useAuthStore();
const router = useRouter();
const isLoggedIn = ref(false);

const checkLoginStatus = async () => {
  isLoggedIn.value = authStore.loggedIn;

  if (!isLoggedIn.value) {
    if (router.currentRoute.value.name !== 'login' && router.currentRoute.value.name !== 'register') {
      router.push({ name: 'login' });
    }
  }
};

const logout = async () => {
  await authStore.logout();
  router.push({ name: 'login' });
};

onMounted(() => {
  checkLoginStatus();
});

watchEffect(() => {
  checkLoginStatus();
});

</script>

<style scoped>
.wrapper {
  margin: 0 auto;
  background: #f8f8f8;
  border-bottom: 1px solid #e1e1e1;
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
  max-height: 65px;
}

.nav-primary {
  width: 960px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  margin: 10px 10px;
}

.nav-primary .brand-logo {
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
  color: #222;
}

.nav-primary ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-primary ul li {
  margin-left: 1rem;
  margin-bottom: 0;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

.nav-primary ul li a {
  text-decoration: none;
  color: #222;
}

.nav-primary ul li:hover {
  background: #e1e1e1;
}
</style>
