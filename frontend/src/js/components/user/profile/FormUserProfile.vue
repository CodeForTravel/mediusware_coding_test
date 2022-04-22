<template>
  <div class="border bg-white p-4 shadow-sm rounded">
    <h5>{{ $t("CHANGE PROFILE") }}</h5>
    <div class="mt-4"></div>
    <b-form @submit.prevent="onFormSubmit">
      <b-form-group :label="$t('Name')">
        <b-form-input
          v-model="user_profile.name"
          type="text"
          placeholder="e.g. John Doe"
        ></b-form-input>
      </b-form-group>

      <b-form-group :label="$t('Email Address')">
        <b-form-input
          v-model="user_profile.email"
          type="email"
          placeholder="e.g. example@email.com"
        ></b-form-input>
      </b-form-group>

      <b-form-group :label="$t('Timezone')" label-class="required">
        <Select2
          v-model="user_profile.timezone"
          :options="timezoneOptions"
          :settings="{ width: '100%' }"
        />
      </b-form-group>

      <b-form-group :label="$t('Timestamp Format')" label-class="required">
        <Select2
          v-model="user_profile.timestamp_format"
          :options="timestampFormatOptions"
          :settings="{ width: '100%' }"
        />
      </b-form-group>

      <b-row class="mt-4">
        <b-col cols="12" class="text-right">
          <b-button type="submit" variant="outline-primary">
            <b>{{ $t("SAVE") }}</b>
          </b-button>
        </b-col>
      </b-row>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const apiClient = axios.create({
  baseURL: process.env.BACKEND_HOST,
});

export default {
  data() {
    return {
      timezone_choices: {},
      timestamp_format_choices: {},

      userId: null,
      user_profile: {
        name: "",
        email: "",
        timezone: "",
        timestamp_format: "",
      },
    };
  },
  components: {},

  created() {
    this.fetchTimezoneChoices();
    this.fetchTimestampFormatChoices();
    this.fetchUserInfo();
  },

  computed: {
    timezoneOptions() {
      var timezone_options = [];

      if (Object.keys(this.timezone_choices).length !== 0) {
        for (const item in this.timezone_choices) {
          timezone_options.push({
            id: item,
            text: item,
          });
        }
      }
      return timezone_options;
    },

    timestampFormatOptions() {
      var timestamp_format_options = [];

      if (Object.keys(this.timestamp_format_choices).length !== 0) {
        Object.keys(this.timestamp_format_choices).forEach((key) => {
          timestamp_format_options.push({
            id: key,
            text: this.timestamp_format_choices[key],
          });
        });
      }

      return timestamp_format_options;
    },
  },

  methods: {
    fetchTimezoneChoices() {
      apiClient
        .get("api/v1/user/profile/timezone/")
        .then((resp) => {
          this.timezone_choices = resp.data.timezone_choices;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    fetchTimestampFormatChoices() {
      apiClient
        .get("api/v1/user/profile/timestamp-format/")
        .then((resp) => {
          this.timestamp_format_choices = resp.data.timestamp_format_choices;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    fetchUserInfo() {
      this.$store.dispatch("user/getUserInfo").then((resp) => {
        if (resp.status == 200) {
          this.userId = resp.data.id;
          this.user_profile.name = resp.data.name;
          this.user_profile.email = resp.data.email;
          this.user_profile.timezone = resp.data.timezone;
          this.user_profile.timestamp_format = resp.data.timestamp_format;
        }
      });
    },

    onFormSubmit() {
      if (["", null].includes(this.user_profile.timezone)) {
        Vue.toasted.show("Select Timezone!", {
          className: "bg-danger",
        });
        return false;
      }
      if (["", null].includes(this.user_profile.timestamp_format)) {
        Vue.toasted.show("Select Timestamp Format!", {
          className: "bg-danger",
        });
        return false;
      }

      this.$store
        .dispatch("user/updateUserProfile", {
          userId: this.userId,
          userProfile: this.user_profile,
        })
        .then((resp) => {});
    },
  },
};
</script>

<style></style>
