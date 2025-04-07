<script setup>
import { ref } from "vue";

const cards = ref([{}, {}, {}]);
</script>

<template>
  <section class="list">
    <div class="list__header">
      <h2>List Header</h2>
      <span>Actions</span>
    </div>
    <div class="list__body">
      <div>
        <Card v-for="card in cards" />
      </div>
    </div>
    <div class="list__footer">
      <span>Actions</span>
      <span>Actions</span>
    </div>
  </section>
</template>

<style scoped>
section.list {
  min-width: 300px;
  background-color: whitesmoke;
  padding: 1rem;
  border-radius: 1rem;
}

.list__header {
  display: flex;
  justify-content: space-between;
}

.list__body {
  background-color: lightgray;
}

.list__footer {
  display: flex;
  justify-content: space-between;
}
</style>
