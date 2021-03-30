<template>
<v-app>
  <div id="app">
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
      }
    },
  },
  data: () => ({
    token: "caaf7dc3b78d8fe1a4b39c4861ae21e133669e8c20c5d56cfbc87872e7ca7e12",
    baseUrl:'http://127.0.0.1:8000/',
  }),
}
</script>

<style>

</style>
