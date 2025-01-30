<template>
  <div class="card">
    <h4>{{ author }}</h4>
    {{ message }}
  </div>
</template>

<script>
export default {
  name: "MessageCard",
  props: {
    author: String,
    message: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card {
  background-color: cadetblue;
  border-radius: 10px;

  text-align: left;
  padding: 1px 10px 10px 10px;
  margin-bottom: 10px;
}
</style>
