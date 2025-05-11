<script setup lang="ts">
import { ref } from "vue";

const lists = ref([
  { title: "Upcoming" },
  { title: "In Progress" },
  { title: "Done" },
]);
</script>

<template>
  <main>
    <div class="board-title">
      <h3>Board Title</h3>
    </div>
    <div class="kanban-board">
      <List v-for="list in lists" :title="list.title" />
    </div>
  </main>
</template>

<style scoped>
main {
  margin: 0;
  padding: 2rem;
  background-color: teal;
  width: 100vw;
  height: 100vh;
}

.kanban-board {
  display: flex;
  gap: 2rem;
}
</style>
