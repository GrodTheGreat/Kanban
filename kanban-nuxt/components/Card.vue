<template>
  <div class="card">
    <div class="card__text">Card Text</div>
    <div class="card__actions">
      <button></button>
      <button></button>
      <button></button>
      <button></button>
    </div>
  </div>
</template>

<style scoped>
.card {
  border-radius: 0.25rem;
  background-color: whitesmoke;
  padding: 0.5rem;
  min-height: 2rem;
  box-shadow: 0 2px 4px black;
}
.card__actions {
  display: flex;
  gap: 0.25rem;
}
</style>
