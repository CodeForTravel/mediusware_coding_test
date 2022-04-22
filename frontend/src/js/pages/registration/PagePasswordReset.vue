<template>
  <div class="my-4">
    <b-row>
      <b-col
        cols="12"
        md="8"
        offset-md="2"
        lg="6"
        offset-lg="3"
        xl="4"
        offset-xl="4"
      >
        <form-password-reset></form-password-reset>
      </b-col>
    </b-row>
  </div>
</template>

<script>
const FormPasswordReset = () =>
  import("../../components/registration/FormPasswordReset.vue");
export default {
  components: {
    FormPasswordReset,
  },
};
</script>

<style></style>
