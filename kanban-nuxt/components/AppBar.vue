<template>
  <header class="app-bar">
    <div class="app-bar__prepend">
      <div class="app-bar__icon">
        <button>Sidebar</button>
      </div>
      <div class="app-bar__title">App Title</div>
    </div>
    <div class="app-bar__append">
      <nav>
        <a href="/login">Login</a>
        <a href="/register">Register</a>
      </nav>
      <div class="app-bar__append--actions">
        <button type="button">Action</button>
        <button type="button">Action</button>
      </div>
      <div class="app-bar__append--overflow">
        <button type="button">Overflow</button>
      </div>
    </div>
  </header>
</template>

<style scoped>
header {
  background-color: blue;
  display: flex;
  justify-content: space-between;
  height: 56px;
  padding: 1rem;
  box-sizing: border-box;
}

.app-bar__prepend {
  display: flex;
  align-content: center;
  height: 100%;
}
.app-bar__icon {
  margin-left: 1rem;
}

.app-bar__title {
  margin-left: 2rem;
}

.app-bar__append {
  display: flex;
}

.app-bar__append--overflow {
  margin-right: 1rem;
}

.app-bar__append--actions {
  margin-right: 1.5rem;
}
</style>
