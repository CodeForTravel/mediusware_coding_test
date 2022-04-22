<template>
  <!-- Nav Item - User Information -->
  <li class="nav-item dropdown no-arrow">
    <a
      class="nav-link dropdown-toggle text-center"
      href="#"
      id="userDropdown"
      role="button"
      data-toggle="dropdown"
      aria-haspopup="true"
      aria-expanded="false"
    >
      <b-img src="/static/icons/user-icon.png" class="img-profile"> </b-img>
    </a>

    <p class="text-center text-gray-600 small">Hello, {{ currentUsername }}</p>

    <!-- Dropdown - User Information -->
    <div
      class="dropdown-menu dropdown-menu-right shadow"
      aria-labelledby="userDropdown"
    >
      <b-link class="dropdown-item" :to="{ name: 'profile' }">
        <i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>
        Profile
      </b-link>

      <div class="dropdown-divider"></div>
      <a class="dropdown-item" href="/logout">
        <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
        Logout
      </a>
    </div>
  </li>
</template>

<script>
import { mapState } from "vuex";

export default {
  created() {
    this.fetchUserInfo();
  },

  computed: {
    ...mapState(["user"]),

    currentUsername() {
      if (this.user.userInfo) {
        if (this.user.userInfo.name) {
          return this.user.userInfo.name;
        } else {
          return this.user.userInfo.username;
        }
      }
    },
  },

  methods: {
    fetchUserInfo() {
      this.$store.dispatch("user/getUserInfo");
    },
  },
};
</script>

<style scoped></style>
