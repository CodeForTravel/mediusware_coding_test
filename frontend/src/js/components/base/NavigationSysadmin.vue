<template>
  <ul
    class="navbar-nav bg-white sidebar sidebar-light accordion"
    id="accordionSidebar"
    :class="{ toggled: settings.isNavToggled }"
  >
    <div class="mt-4"></div>
    <!-- Sidebar - Brand -->
    <b-link
      class="sidebar-brand d-flex align-items-center justify-content-center"
      :to="{ name: 'dashboard' }"
    >
      <div>
        <img src="/static/img/MediuswareLogo.png" alt="analytic" width="80%" />
      </div>
    </b-link>

    <div class="text-center mt-4">
      <small>SYSADMIN PANEL</small>
    </div>

    <!-- Divider -->
    <hr class="sidebar-divider my-2" />

    <!-- Nav Item - Dashboard -->
    <li
      :class="this.$route.name == 'dashboard' ? 'nav-item active' : 'nav-item'"
    >
      <b-link
        :class="
          this.$route.name == 'dashboard' ? 'nav-link' : 'nav-link collapsed'
        "
        :to="{ name: 'dashboard' }"
      >
        <i class="fas fa-fw fa-tachometer-alt"></i>
        <span>DASHBOARD</span>
      </b-link>
    </li>

    <!-- Divider -->
    <hr class="sidebar-divider" />

    <!-- Settings Links -->
    <li :class="getLiActiveClass(settingsRouteList)">
      <b-link
        :class="getBlinkCollapsedClass(settingsRouteList)"
        href="#"
        data-toggle="collapse"
        data-target="#collapseThree"
        :aria-expanded="isBlinkAreaExpanded(settingsRouteList)"
        aria-controls="collapseThree"
      >
        <i class="fas fa-cog text-primary"></i>
        <span>SETTINGS</span>
      </b-link>
      <div
        id="collapseThree"
        :class="getDivCollapsedClass(settingsRouteList)"
        aria-labelledby="headingTwo"
        data-parent="#accordionSidebar"
      >
        <div class="bg-white collapse-inner">
          <b-link
            :class="
              this.$route.name == 'sysadmin-general-settings'
                ? 'collapse-item active'
                : 'collapse-item'
            "
            :to="{ name: 'sysadmin-general-settings' }"
            >GENERAL</b-link
          >
        </div>
      </div>
    </li>

    <!-- Divider -->
    <hr class="sidebar-divider d-none d-md-block mt-1" />

    <sysadmin-user-menu></sysadmin-user-menu>

    <hr class="sidebar-divider d-none d-md-block" />

    <!-- Sidebar Toggler (Sidebar) -->
    <div class="mt-3 text-center d-none d-md-inline">
      <button
        class="rounded-circle border-0"
        id="sidebarToggle"
        @click="toggleNav"
      ></button>
    </div>
  </ul>
</template>

<script>
import { mapState, mapMutations } from "vuex";

const SysadminUserMenu = () => import("./SysadminUserMenu.vue");

export default {
  components: { SysadminUserMenu },

  data() {
    return {
      settingsRouteList: ["sysadmin-general-settings"],
    };
  },

  computed: {
    ...mapState(["settings"]),
  },

  methods: {
    ...mapMutations("settings", ["TOGGLE_NAV"]),

    toggleNav() {
      this.TOGGLE_NAV();
    },

    getLiActiveClass(routeNameList) {
      let classStr = "nav-item";
      let routeMatched = false;

      for (const routeName of routeNameList) {
        if (this.$route.name == routeName) {
          routeMatched = true;
          break;
        }
      }

      if (routeMatched) {
        classStr = "nav-item active";
      }

      return classStr;
    },

    getBlinkCollapsedClass(routeNameList) {
      let classStr = "nav-link";
      let routeMatched = false;

      for (const routeName of routeNameList) {
        if (this.$route.name == routeName) {
          routeMatched = true;
          break;
        }
      }

      if (!routeMatched) {
        classStr = "nav-link collapsed";
      }

      return classStr;
    },

    getDivCollapsedClass(routeNameList) {
      let classStr = "collapse";
      let routeMatched = false;

      for (const routeName of routeNameList) {
        if (this.$route.name == routeName) {
          routeMatched = true;
          break;
        }
      }

      if (routeMatched) {
        classStr = "collapse show";
      }

      return classStr;
    },

    isBlinkAreaExpanded(routeNameList) {
      let routeMatched = false;

      for (const routeName of routeNameList) {
        if (this.$route.name == routeName) {
          routeMatched = true;
          break;
        }
      }

      if (!routeMatched) {
        return false;
      } else {
        return true;
      }
    },
  },
};
</script>

<style scoped>
.nav-main {
  margin-top: -5px;
}
</style>
