import Vue from "vue";
import Select2 from "v-select2-component";
import Toasted from "vue-toasted";
import i18n from "../i18n.js";
import * as filters from "../filters.js";
import store from "./store";
import router from "./router";

const NavigationSysadmin =()=> import("./components/base/NavigationSysadmin.vue")
const TopBar =()=> import("./components/base/TopBar.vue")

import {
  LayoutPlugin,
  BCard,
  BNav,
  BAlert,
  BButton,
  BForm,
  BFormInput,
  BFormGroup,
  BLink,
  BImg,
  BRow,
  BCol,
  VBModal,
  BModal,
  BPagination,
  BTable,
  BIcon,
  BSpinner,
  BFormCheckbox
} from "bootstrap-vue";


//bootstrap components
Vue.component("BCard", BCard);
Vue.component("BNav", BNav);
Vue.component("BAlert", BAlert);
Vue.component("BButton", BButton);
Vue.component("BForm", BForm);
Vue.component("BFormInput", BFormInput);
Vue.component("BFormGroup", BFormGroup);
Vue.component("BLink", BLink);
Vue.component("BImg", BImg);
Vue.component("BRow", BRow);
Vue.component("BCol", BCol);
Vue.component("BModal", BModal);
Vue.component("BPagination", BPagination);
Vue.component("BTable", BTable);
Vue.component("BIcon", BIcon);
Vue.component("BSpinner", BSpinner);
Vue.component("BFormCheckbox", BFormCheckbox);




// bootstrap directives
Vue.directive("b-modal", VBModal);


Vue.component("Select2", Select2);

window.Vue = Vue;

Vue.use(Toasted, {
  class: "rounded",
  position: "bottom-right",
  fitToScreen: true,
  theme: "toasted-primary",
  duration: 4000,
});

const app = new Vue({
  el: "#app",
  i18n,
  router,
  store,
  components: {
    NavigationSysadmin,
    TopBar
  },
});
