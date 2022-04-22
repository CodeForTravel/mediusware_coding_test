import SettingsService from "../../service/settings/SettingsService.js";

export const namespaced = true;

export const state = {
  isNavToggled: false,

  paginationData: {
    TableEventLogs: 20,
  },
};

export const mutations = {
  TOGGLE_NAV(state) {
    state.isNavToggled = !state.isNavToggled;
  },

  SET_PAGINATION(state, { paginationKey, paginationSize }) {
    localStorage.setItem(paginationKey, paginationSize);
    state.paginationData[paginationKey] = paginationSize;
  },

  GET_PAGINATION(state, paginationKey) {
    let newPaginationSize = localStorage.getItem(paginationKey);
    if (newPaginationSize && newPaginationSize != "undefined") {
      state.paginationData[paginationKey] = newPaginationSize;
    }
  },
};

export const actions = {

};
