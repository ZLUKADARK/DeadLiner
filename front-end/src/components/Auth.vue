<template>
<div>
  <v-row justify="center">
    <v-dialog persistent v-model="dialog" max-width="600">
<template v-if="registration">
  <v-card elevation="28">
        <v-card-title class="headline"> Регистрация </v-card-title>

        <v-card-text>
          <div>
            <v-text-field
              label="Email"
              v-model="email"
              :rules="rules"
              hide-details="auto"
            ></v-text-field>
            <v-text-field
              label="Username"
              v-model="username"
              :rules="rules"
              hide-details="auto"
            ></v-text-field>
            <v-text-field
              label="Password"
              v-model="password"
              :rules="rules"
              hide-details="auto"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>
          </div>
        </v-card-text>

        <v-card-actions>
         

          <v-btn color="#C0CA33" text @click="registraid()">
            Подтвердить
          </v-btn>
 <v-spacer></v-spacer>
          <v-btn color="#00E5FF" text @click="registration = false">
            Назад =>
          </v-btn> 
        </v-card-actions>
      </v-card>
</template>
<template v-else>

      <v-card elevation="28">
        <v-card-title  class="headline"> Авторизация </v-card-title>

        <v-card-text>
          <div>
            <v-text-field
              label="Username"
              v-model="username"
              :rules="rules"
              hide-details="auto"
            ></v-text-field>
            <v-text-field
              label="Password"
              v-model="password"
              :rules="rules"
              hide-details="auto"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>
          </div>
        </v-card-text>

        <v-card-actions>
         

          <v-btn color="#C0CA33" text @click="registration=true">
            Зарегистрироваться
          </v-btn>
 <v-spacer></v-spacer>
          <v-btn color="#00E5FF" text @click="authorize()">
            Авторизоваться
          </v-btn>
        </v-card-actions>
      </v-card>
  </template>
  </v-dialog>
  </v-row>
  </div>
</template>

<script>

export default {
  name: "Auth",
  props: ["baseUrl" ],
  methods: {
    authorize: function () {
      let this_ = this
      this.axios
        .post(`${this.baseUrl}api/login/`, {
          username: this.username,
          password: this.password,
        })
        .then( response => {
          this_.$emit('auth', response.data)
        })
        .catch( error => {
          console.error(error)
          alert('Ошибка. Для деталей см консоль')
        });
    },
    registraid: function () {
      let this_ = this
      this.axios
        .post(`${this.baseUrl}api/register/`, {
          username: this.username,
          password: this.password,
          email: this.email,
        })
        .then( response => {
          this_.$emit('auth', response.data)
        })
        .catch( error => {
          console.error(error);
          alert('Ошибка. Для деталей см консоль')
        });
    },
  },
  data: () => ({
    rules: [
      (value) => !!value || "Required.",
      (value) => (value && value.length >= 3) || "Min 3 characters",
    ],
    registration: false,
    dialog: true,
    username: null,
    password: null,
    email: null,
    show1: false,
  }),
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
