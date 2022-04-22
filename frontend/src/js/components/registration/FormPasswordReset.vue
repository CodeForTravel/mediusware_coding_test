<template>
  <div class="my-4">
    <div class="card">
      <b-form @submit.prevent="onFormSubmit">
        <div class="card-header">
          <h5>Password Reset</h5>
        </div>

        <div class="card-body">
          <b-row>
            <b-col cols="12">
              <b-form-group label="Email" label-class="required">
                <b-form-input
                  type="email"
                  placeholder="e.g. johndoe@gmail.com"
                  maxlength="254"
                  autocomplete="email"
                  required
                  v-model="email"
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col cols="12" class="text-right">
              <b-button type="submit" variant="primary" :disabled="onProgress">
                <b>{{ $t("SUBMIT") }}</b>
              </b-button>
            </b-col>
          </b-row>
        </div>
      </b-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      onProgress: false,
      email: null,
    };
  },
  methods: {
    onFormSubmit() {
      if (["", null].includes(this.email)) {
        Vue.toasted.error("Email required!");
        return false;
      }
      this.onProgress = true;
      this.$store
        .dispatch("registration/resetPassword", { email: this.email })
        .then((resp) => {
          this.onProgress = false;
          this.sendToPasswordResetDonePage();
        });
    },
    sendToPasswordResetDonePage() {
      let new_path = window.location.origin + `/account/password_reset/done`;
      window.location = new_path;
    },
  },
};
</script>

<style scoped></style>
