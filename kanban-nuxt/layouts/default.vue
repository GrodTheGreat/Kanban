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
  z-index: 3;
  box-shadow: 0 1px 4px black;
}

.side {
  grid-area: sidebar;
  z-index: 2;
  box-shadow: 1px 0 4px black;
}

.main {
  grid-area: main;
  z-index: 1;
}

.foot {
  grid-area: footer;
  z-index: 1;
}
</style>
