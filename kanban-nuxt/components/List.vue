<script setup lang="ts">
import { ref } from "vue";

defineProps<{ title: string }>();

const cards = ref([{}, {}, {}]);
</script>

<template>
  <section class="list">
    <div class="list__header">
      <h2>{{ title }}</h2>
      <span>
        <button>...</button>
      </span>
    </div>
    <div class="list__body">
      <div class="list__cards">
        <Card v-for="card in cards" />
      </div>
    </div>
    <div class="list__footer">
      <span>
        <button>+ Add another card</button>
      </span>
      <span>
        <button>Actions</button>
      </span>
    </div>
  </section>
</template>

<style scoped>
section.list {
  min-width: 300px;
  background-color: lightgray;
  padding: 1rem;
  border-radius: 0.5rem;
}

.list__header {
  display: flex;
  justify-content: space-between;
}

.list__body {
  background-color: lightgray;
}

.list__cards {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.list__footer {
  display: flex;
  justify-content: space-between;
}
</style>
