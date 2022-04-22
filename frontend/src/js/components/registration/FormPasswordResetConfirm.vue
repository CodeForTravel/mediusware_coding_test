<template>
  <div class="my-4">
    <div class="card">
      <b-form @submit.prevent="onFormSubmit" @reset.prevent="onFormReset">
        <div class="card-header">
          <h5>Change Password</h5>
        </div>
        <div class="card-body">
          <b-row>
            <b-col cols="12">
              <b-form-group label="New Password" label-class="required">
                <b-form-input
                  type="password"
                  placeholder="New Password"
                  required
                  v-model="password1"
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col cols="12">
              <b-form-group label="Confirm Password" label-class="required">
                <b-form-input
                  type="password"
                  placeholder="Confirm Password"
                  required
                  v-model="password2"
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col cols="6">
              <b-button type="reset" variant="danger" :disabled="onProgress">
                <b>{{ $t("RESET") }}</b>
              </b-button>
            </b-col>
            <b-col cols="6" class="text-right">
              <b-button type="submit" variant="primary" :disabled="onProgress">
                <b>{{ $t("SAVE") }}</b>
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
      token: null,
      password1: null,
      password2: null,
    };
  },
  created() {
    this.token = this.$route.params.token;
  },
  methods: {
    onFormSubmit() {
      this.onProgress = true;
      if (this.password1 === this.password2) {
        this.$store
          .dispatch("registration/resetPasswordConfirm", {
            password: this.password1,
            token: this.token,
          })
          .then((response) => {
            this.onProgress = false;
            if (response.status == 200) {
              this.resetForm();
              this.sendToPasswordResetCompletePage();
            }
          });
      } else {
        this.onProgress = false;
        Vue.toasted.show("Passwords don't match", {
          className: "bg-danger",
        });
      }
    },
    sendToPasswordResetCompletePage() {
      let new_path = window.location.origin + `/account/reset/done`;
      window.location = new_path;
    },
    resetForm() {
      this.password1 = null;
      this.password2 = null;
    },
  },
};
</script>

<style scoped></style>
