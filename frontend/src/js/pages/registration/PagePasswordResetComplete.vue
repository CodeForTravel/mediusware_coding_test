<template>
  <div class="my-4">
    <b-row>
      <b-col cols="12" md="8" offset-md="2" lg="8" offset-lg="2">
        <div class="my-4">
          <div class="card">
            <div class="card-body">
              <b-row>
                <b-col cols="12">
                  <p class="text-center">
                    Your password has been set. You may go ahead and
                    <b-link :to="{ name: 'login' }"><b>Login</b></b-link> now.
                  </p>
                </b-col>
              </b-row>
            </div>
          </div>
        </div>
      </b-col>
    </b-row>
  </div>
</template>
