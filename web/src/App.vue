<template>
  <header>
    <div class="wrapper">
      <nav class="nav-primary">
        <RouterLink to="/" class="brand-logo">MySite</RouterLink>
        <ul>
          <li><RouterLink to="/">Home</RouterLink></li>
        </ul>
      </nav>
    </div>
  </header>

  <div class="container">
    <RouterView />
  </div>
</template>

<script setup>
</script>

<style scoped>
.wrapper {
  margin: 0 auto;
  background: #f8f8f8;
  border-bottom: 1px solid #e1e1e1;
  display: flex;
  justify-content: center;
}

.nav-primary {
  width: 960px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
}

.nav-primary .brand-logo {
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
  color: #333;
}

.nav-primary ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-primary ul li {
  margin-left: 1rem;
}

.nav-primary ul li a {
  text-decoration: none;
  color: #333;
  padding: 0.5rem 1rem;
  transition: background 0.3s;
}

.nav-primary ul li a:hover {
  background: #e1e1e1;
}
</style>
