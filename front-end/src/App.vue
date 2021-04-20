<template>
<v-app>
  <div id="app">
    <template>
  <v-tabs
    fixed-tabs
    background-color="indigo"
    dark
  >
    <v-tab @click="logmenu()">
     Выйти
    </v-tab>
  </v-tabs>
</template>
    <template v-if="!token">
      <Auth @auth='authByToken' :baseUrl="baseUrl"/>
    </template>
    <template v-else >
      <TaskList :baseUrl="baseUrl" :token="token"/>
    </template>
  </div>
</v-app>
</template>

<script>
import TaskList from './components/TaskList.vue'
import Auth from './components/Auth.vue'
export default {
  name: 'App',
  components: {
    TaskList,
    Auth,
  },
  methods:{
    authByToken: function(response){
      if(response.token){
        this.token = response.token
        console.log(response.token)
      }
    },
    logmenu: function (){
      this.token = null
      }
    },

  

  data: () => ({
    token: null,
    baseUrl:'http://127.0.0.1:8000/',
  }),
}
</script>

<style>

</style>
