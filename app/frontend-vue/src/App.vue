<template>
  <!-- Top panel -->
  <nav class="top-menu">
    <ul>
      <li>
        <p class="title-container">Message Board</p>
      </li>
      <!-- <li>
        <div class="debug-info">
          <ul>
            <li>backend: {{ backendWorker }}</li>
            <li>xyz</li>
          </ul>
        </div>
      </li> -->
    </ul>
  </nav>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.top-menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  background-color: #333;
  color: white;
  display: flex;
  align-items: center; /* Ensures vertical centering */
  justify-content: space-between;
  padding: 0;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  z-index: 1000;
}

.top-menu.title-container {
  font-size: 24px;
  font-weight: bold;
}

.top-menu ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.top-menu ul li {
  margin: 0 15px;
}

/* Add padding to body to prevent content from being hidden under the fixed menu */
body {
  padding-top: 60px; /* Should match the height of the menu */
}
</style>
