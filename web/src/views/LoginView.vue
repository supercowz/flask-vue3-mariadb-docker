<template>
  <div class="row">
    <div class="one-half column offset-by-three">
      <form @submit.prevent="login">
        <h4>Login</h4>
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" class="u-full-width">
        
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" class="u-full-width">
        
        <button type="submit" class="button-primary u-full-width">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      console.log(`Username: ${this.username}, Password: ${this.password}`);
    }
  }
}
</script>

<style scoped>
</style>
