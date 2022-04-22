<template>
  <b-nav
    class="navbar navbar-expand navbar-light bg-white topbar static-top shadow-sm top_wrapper"
  >
    <!-- Sidebar Toggle (Topbar) -->
    <button
      id="sidebarToggleTop"
      class="btn btn-link d-md-none rounded-circle mr-3"
      @click="toggleNav()"
    >
      <i class="fa fa-bars"></i>
    </button>

    <ul
      class="navbar-nav d-none d-sm-inline-block form-inline mr-auto ml-md-2 my-2 my-md-0 mw-100"
    >
      <h4 class="card-header-title mt-2 font-weight-bold">
        {{ navBarTitle }}
      </h4>
    </ul>
    <img src="/static/img/MediuswareLogo.png" width="12%" alt="Mediusware" />
  </b-nav>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  computed: {
    navBarTitle() {
      return this.$route.meta.navBarTitle;
    },
  },

  methods: {
    ...mapMutations("settings", ["TOGGLE_NAV"]),

    toggleNav() {
      this.TOGGLE_NAV();
    },
  },
};
</script>

<style scoped>
.top_wrapper {
  margin: 0 -5px;
}
</style>
