<template>
  <div class="my-4">
    <b-row>
      <b-col cols="12" class="text-center mb-4">
        <div class="login-brand">
          <img class="login_page_logo" src="/static/img/mediusware_logo.png" alt="logo" />
          <h5 class="my-4 login_page_header">
            <!-- Mediusware -->
          </h5>
        </div>
      </b-col>
      <b-col cols="12" xl="4" lg="6" class="mx-auto">
        <form-login></form-login>
      </b-col>
    </b-row>
  </div>
</template>

<script>
const FormLogin = () => import("../../components/user/auth/FormLogin.vue");

export default {
  components: {
    FormLogin,
  },
};
</script>

<style>
.login_page_logo{
  height: 80%;
  width: 15%;
}
.login_page_header{
  letter-spacing: 3px;
  font-size: 50px;
  font-weight: 600;
}
</style>
