<template>
<v-app>
  <div id="app">
    <template>
  <v-app-bar color="#DCE775">

    <v-tab><h2>DeadLiner</h2></v-tab>
    <v-spacer></v-spacer>


    <v-tab >
      <v-btn 
      @click="logmenu()"
      color="#D4E157"
      elevation="2"
      >
      Выйти
      </v-btn>
     
    </v-tab>
  </v-app-bar>
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
        localStorage.token = response.token
        this.token = localStorage.token
      }
    },
    logmenu: function (){
      this.token = null
      localStorage.token = 0
      }
    },

  

  data: () => ({
    token: localStorage.token == 0 ? null : localStorage.token,
    baseUrl:'http://127.0.0.1:8000/',
  }),
}
</script>

<style>


</style>
