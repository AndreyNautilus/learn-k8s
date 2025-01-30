<template>
  <div class="home">
    <!-- List of messages -->
    <div>
      <h2>List of existing messages</h2>
      <div v-for="m in messages">
        <MessageCard :author="m.author" :message="m.text" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MessageCard from "@/components/MessageCard.vue";

// TODO: remove me, it's just for local checking
const testData = [
  {
    author: "Fake User 1",
    text: "Fake message 1",
  },
  {
    author: "Fake User 2",
    text: "Fake message 2",
  },
];

export default {
  name: "HomeView",
  components: {
    MessageCard,
  },
  data() {
    return {
      messages: [],
    };
  },
  mounted() {
    fetch("/api/posts")
      .then((res) => res.json())
      .then((data) => (this.messages = data))
      .catch((err) => {
        this.messages = [
          {
            author: "no author",
            text: "no message",
          },
        ];
        console.log(err.message);
      });
  },
};
</script>
