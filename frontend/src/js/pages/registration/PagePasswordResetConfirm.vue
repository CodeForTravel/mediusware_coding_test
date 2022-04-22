<template>
  <div class="my-4">
    <b-row>
      <b-col v-if="!isTokenValid" cols="12">
        <div class="my-4">
          <div class="card">
            <div class="card-body">
              <p class="text-center">
                The password reset link was invalid, possibly because it has
                already been used. Please request a new password reset.
              </p>
            </div>
          </div>
        </div>
      </b-col>
      <b-col v-else cols="12" md="8" offset-md="2" lg="6" offset-lg="3">
        <form-password-reset-confirm></form-password-reset-confirm>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import FormPasswordResetConfirm from "../../components/registration/FormPasswordResetConfirm.vue";
export default {
  components: {
    FormPasswordResetConfirm,
  },
  data() {
    return {
      isTokenValid: false,
    };
  },
  created() {
    this.validateToken();
  },
  methods: {
    validateToken() {
      this.$store
        .dispatch("registration/resetPasswordValidateToken", {
          token: this.$route.params.token,
        })
        .then((resp) => {
          if (resp.status == 200) {
            this.isTokenValid = true;
          }
        });
    },
  },
};
</script>

<style scoped></style>
