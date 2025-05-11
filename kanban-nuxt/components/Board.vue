<script setup lang="ts">
import { ref } from "vue";

const lists = ref([
  { title: "Upcoming" },
  { title: "In Progress" },
  { title: "Done" },
]);
</script>

<template>
  <div class="board">
    <div class="board__title">
      <h3>Board Title</h3>
    </div>
    <div class="board__content">
      <List v-for="list in lists" :title="list.title" />
    </div>
  </div>
</template>

<style scoped>
.board {
  margin: 0;
  padding: 2rem;
  background-color: teal;
  height: 100%;
}

.board__content {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
}
</style>
