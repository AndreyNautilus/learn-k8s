<template>
  <div class="home">
    <div id="post_form">
      <form @submit.prevent="submitMessage" class="message-form">
        <h2>Post a new message</h2>
        <div class="form-group">
          <label for="author">Author:</label>
          <input
            type="text"
            id="author"
            v-model="formData.author"
            required
            class="form-input"
          >
        </div>
        <div class="form-group">
          <label for="message">Message:</label>
          <textarea
            id="message"
            v-model="formData.message"
            required
            class="form-input"
            rows="3"
          ></textarea>
        </div>
        <button type="submit" class="submit-button">Post</button>
      </form>
    </div>
    <!-- List of messages -->
    <div class="list-of-messages">
      <h2>List of existing messages</h2>
      <div v-for="m in messages" :key="m.id">
        <MessageCard :author="m.author" :message="m.text" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MessageCard from "@/components/MessageCard.vue";

export default {
  name: "HomeView",
  components: {
    MessageCard,
  },
  data() {
    return {
      messages: [],
      formData: {
        author: "",
        message: ""
      }
    };
  },
  methods: {
    submitMessage() {
      const payload = {
        author: this.formData.author,
        text: this.formData.message
      };

      fetch("/api/posts", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      })
        .then((res) => {
          if (!res.ok) throw new Error("Failed to post message");
          return res.json().catch(() => null);
        })
        .then(() => {
          this.messages.unshift(payload);
        })
        .catch((err) => {
          console.error(err);
        })
        .finally(() => {
          // clear the form in all cases
          this.formData.author = "";
          this.formData.message = "";
        });
    }
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

<style scoped>
.message-form {
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;

  /* make children stack and allow left alignment */
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.form-group {
  margin-bottom: 15px;
  /* ensure inputs stay full width inside the flex column */
  width: 100%;
}

.form-group label {
  text-align: left;
  display: block;
  margin-bottom: 5px;
}

.form-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

/* ensure textarea has a minimum height (approx. 3 lines) and can be resized vertically */
textarea.form-input {
  min-height: 3em;
  resize: vertical;
}

.submit-button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;

  /* explicitly left-align the button within the form */
  align-self: flex-start;
}

.submit-button:hover {
  background-color: #45a049;
}

.list-of-messages h2 {
  text-align: left;
}
</style>
