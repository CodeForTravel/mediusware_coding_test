import Vue from "vue";
import Router from "vue-router";

const PageDashboard = () => import("../pages/dashboard/PageDashboard.vue");
const PageUserProfile = () => import("../pages/user/PageUserProfile.vue");
const PageLogin = () => import("../pages/auth/PageLogin.vue");
const PagePasswordReset = () =>
  import("../pages/registration/PagePasswordReset.vue");
const PagePasswordResetDone = () =>
  import("../pages/registration/PagePasswordResetDone.vue");
const PagePasswordResetComplete = () =>
  import("../pages/registration/PagePasswordResetComplete.vue");
const PagePasswordResetConfirm = () =>
  import("../pages/registration/PagePasswordResetConfirm.vue");
const PageSettingsSysadminGeneral = () =>
  import("../pages/settings/sys_admin/PageSettingsSysadminGeneral.vue");

Vue.use(Router);

const routes = [
  {
    path: "/user/profile/",
    name: "profile",
    component: PageUserProfile,
    props: true,
    meta: { title: "Profile | Mediusware", navBarTitle: "Profile" },
  },

  {
    path: "/login/",
    name: "login",
    component: PageLogin,
    props: true,
    meta: { title: "Mediusware" },
  },

  {
    path: "/change-weak-password/",
    name: "change-weak-password",
    meta: {
      title: "Change Password | Mediusware",
    },
  },
  {
    path: "/account/password_reset",
    name: "password-reset",
    component: PagePasswordReset,
    props: true,
    meta: {
      title: "Password Reset | Mediusware",
      navBarTitle: "Password Reset",
    },
  },
  {
    path: "/account/password_reset/done/",
    name: "password-reset-done",
    component: PagePasswordResetDone,
    meta: {
      title: "Password Reset Done | Mediusware",
    },
  },
  {
    path: "/account/reset/done/",
    name: "password-reset-complete",
    component: PagePasswordResetComplete,
    meta: {
      title: "Password Reset Complete | Mediusware",
    },
  },
  {
    path: "/account/reset/:token/confirm",
    name: "password-reset-confirm",
    component: PagePasswordResetConfirm,
    props: true,
    meta: {
      title: "Password Reset Confirm | Mediusware",
    },
  },

  // sysadmin panel router
  {
    path: "/dashboard/",
    name: "dashboard",
    component: PageDashboard,
    props: true,
    meta: { title: "Dashboard | Mediusware", navBarTitle: "Dashboard" },
  },
  {
    path: "/settings/sysadmin/general/",
    name: "sysadmin-general-settings",
    component: PageSettingsSysadminGeneral,
    props: true,
    meta: {
      title: "General Settings | Mediusware",
      navBarTitle: "General Settings",
    },
  },
];

const router = new Router({
  mode: "history",
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
