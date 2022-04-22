<template>
  <div class="border bg-white p-4 shadow-sm rounded">
    <h5>{{ $t("CHANGE PASSWORD") }}</h5>
    <div class="mt-4"></div>

    <b-form @submit.prevent="onFormSubmit" @reset.prevent="resetForm">
      <b-form-group label="Old Password" label-class="required">
        <b-form-input
          type="password"
          placeholder="Old Password"
          required
          v-model="old_password"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="New Password" label-class="required">
        <b-form-input
          type="password"
          placeholder="New Password"
          required
          v-model="password1"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Confirm Password" label-class="required">
        <b-form-input
          type="password"
          placeholder="Confirm Password"
          required
          v-model="password2"
        ></b-form-input>
      </b-form-group>

      <b-row class="mt-4">
        <b-col cols="6">
          <b-button
            type="reset"
            variant="outline-danger"
            size="md"
            :disabled="onProgress"
          >
            <b>{{ $t("RESET") }}</b>
          </b-button>
        </b-col>
        <b-col cols="6" class="text-right">
          <b-button
            type="submit"
            variant="outline-primary"
            size="md"
            :disabled="onProgress"
          >
            <b>{{ $t("SAVE") }}</b>
          </b-button>
        </b-col>
      </b-row>
    </b-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      onProgress: false,

      password1: null,
      password2: null,
      old_password: null,
    };
  },

  methods: {
    onFormSubmit() {
      this.onProgress = true;

      if (this.password1 === this.password2) {
        let passwordData = {
          new_password: this.password1,
          old_password: this.old_password,
        };

        this.$store
          .dispatch("user/changeUserPassword", passwordData)
          .then((response) => {
            this.onProgress = false;

            if (response.status == 200) {
              this.resetForm();

              setTimeout(function() {
                window.location.href = "/logout";
              }, 3000);
            }
          });
      } else {
        this.onProgress = false;
        Vue.toasted.show("Passwords don't match", {
          className: "bg-danger",
        });
      }
    },

    resetForm() {
      this.password1 = null;
      this.password2 = null;
      this.old_password = null;
    },
  },
};
</script>

<style scoped></style>
