<template>
  <b-card class="card">
    <div class="card-header"><h5>Login</h5></div>

    <div class="card-body">
      <b-form
        @submit.prevent="onFormSubmit"
        @reset="onFormReset"
        class="needs-validation"
        novalidate=""
      >
        <b-form-group :label="$t('Username')" label-class="required">
          <b-form-input
            v-model="form.username"
            type="text"
            required
            placeholder="Username"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group :label="$t('Password')" label-class="required">
          <b-form-input
            v-model="form.password"
            type="password"
            required
            placeholder="Password"
          >
          </b-form-input>
          <div class="d-block">
            <div class="float-right">
              <b-link @click="sendToForgotPasswordPage">
                Forgot password?
              </b-link>
            </div>
          </div>
        </b-form-group>

        <div class="form-group">
          <b-button
            type="submit"
            class="btn btn-primary btn-md btn-block"
            :disabled="isProcessing"
          >
            <b>LOGIN</b>
            <b-spinner v-if="isProcessing" small></b-spinner>
          </b-button>
        </div>
      </b-form>
    </div>
  </b-card>
</template>

<script>
export default {
  data() {
    return {
      isProcessing: false,
      form: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    onFormSubmit() {
      if (["", null].includes(this.form.username)) {
        Vue.toasted.show("Enter username!", {
          className: "bg-danger",
        });
        return false;
      }

      if (["", null].includes(this.form.password)) {
        Vue.toasted.show("Enter password!", {
          className: "bg-danger",
        });
        return false;
      }

      this.isProcessing = true;

      this.$store.dispatch("user/userLogin", this.form).then((resp) => {
        this.isProcessing = false;
        if (resp.status == 200) {
          let new_path = window.location.origin + `${resp.data.redirect_url}`;
          window.location = new_path;
        }
      });
    },

    sendToForgotPasswordPage() {
      let new_path = window.location.origin + `/account/password_reset`;
      window.location = new_path;
    },

    resetForm() {
      this.form.username = "";
      this.form.password = "";
    },

    onFormReset() {
      this.resetForm();
    },
  },
};
</script>

<style></style>
