<template>
  <div class="row">
    <div class="one-half column offset-by-three">
      <form @submit.prevent="register">
        <h4>Register</h4>
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" class="u-full-width">
        
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" class="u-full-width">

        <label for="confirmPassword">Confirm Password</label>
        <input type="password" id="confirmPassword" class="u-full-width">
        
        <button type="submit" class="button-primary u-full-width">Register</button>
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
    register() {
      console.log(`Username: ${this.username}, Password: ${this.password}`);
    }
  }
}
</script>

<style scoped>
</style>
