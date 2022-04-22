<template>
  <div>
    <Home />
  </div>
</template>

<script>
const Home = () => import("../components/home/Home.vue");
export default {
  components: {
    Home,
  },
};
</script>

<style></style>
