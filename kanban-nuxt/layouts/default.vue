<template>
  <div class="layout">
    <AppBar class="bar" />
    <Sidebar class="side" />
    <main class="main">
      <slot />
    </main>
    <Footer class="foot" />
  </div>
</template>

<style scoped>
.layout {
  display: grid;
  grid-template-areas:
    "appbar appbar"
    "sidebar main"
    "sidebar footer";
  grid-template-columns: 300px 1fr;
  grid-template-rows: auto 1fr auto;
  height: 100vh;
}

.bar {
  grid-area: appbar;
}

.side {
  grid-area: sidebar;
}

.main {
  grid-area: main;
}

.foot {
  grid-area: footer;
}
</style>
