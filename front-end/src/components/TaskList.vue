<template>
  <div >
    <TaskDetail v-if="dialogItem" :item="dialogItem" @return="proceedButton" :baseUrl="baseUrl" :token="token"/>
    <v-card style="margin-top: 25px" max-width="80%" class="mx-auto">
      <v-card-text>
        <v-data-table :headers="tableHeaders" :items="taskList" item-key="id" :hide-default-footer="true" :items-per-page="9999">

          <template v-slot:top >
            <div class="justify-end">
            <v-btn small text color="primary" @click="dialogItem = {}"> <v-icon> mdi-plus-box </v-icon></v-btn>
            </div>
          </template>

          <template v-slot:[`item.details`]="{ item }">
            <v-btn small color="primary" text v-if="item.id" @click="show(item)" > Детально </v-btn>
          </template>

          <template v-slot:[`item.deadline`]="{ item }">
            {{formatDate(item.deadline)}}
          </template>

          <template v-slot:[`item.timeleft`]="{ item }">
            {{calcRemainingTime(item.deadline)}}
          </template>

          <template v-slot:[`item.completed`]="{ item }">
            {{item.completed ? 'Завершена' : 'В процессе'}}
          </template>

          <template v-slot:[`item.complete`]="{ item }">
            <v-btn small color="primary" text v-if="item.id && !item.completed" >Завершить</v-btn>
          </template>

          <template v-slot:[`item.delete`]="{ item }">
            <v-btn small color="error" text v-if="item.id" @click="deleteRecord(item)"><v-icon> mdi-delete-forever</v-icon></v-btn>
          </template>
          
        </v-data-table>
        
      </v-card-text>
    </v-card>
  </div>

</template>

<script>
import TaskDetail from './TaskDetail.vue'

export default {
  name: "TaskList",
  components:{
    TaskDetail,
  },
  props: ["baseUrl", "token"],
  mounted: function () {
    this.getTaskList();

  },
  methods: {
    getTaskList: function () {
      let this_ = this;
      this.axios
        .get(`${this.baseUrl}task-list/`, {
          headers: {
            Authorization: `Token ${this.token}`,
          },
        })
        .then(function (response) {
          this_.taskList = response.data;
        })
        .catch(function (error) {
          console.error(error);
        })
        .then(function () {});
    },
    prepareList: function () {
      return this.taskList.filter((item) => {
        if (item.completed == true && this.showComplete) return item;
        if (item.completed == false && this.showIncomplete) return item;
      });
    },
    calcRemainingTime: function (deadline) {
      let today = new Date();
      deadline = new Date(deadline);
      if (today >= deadline) {
        let timeleft = Math.abs(today.getTime() - deadline.getTime());
        timeleft = Math.ceil(timeleft / (1000 * 60 * 60 * 24));
        return `Просрочено на ${timeleft} д.`;
      } else {
        let timeleft = Math.abs(deadline.getTime() - today.getTime());
        timeleft = Math.ceil(timeleft / (1000 * 60 * 60 * 24));
        return `Осталось ${timeleft} д.`;
      }
    },
    show: function(item) {
      this.dialogItem = item
    },
    proceedButton: function(result) {
      if (typeof(result) == 'object') {
        let found = false

        let tmp = this.taskList
        
        for(let i = 0; i < tmp.length; i++) {
          if (tmp[i].id == result.id) {
            tmp[i] = result
            found = true
          }
        }
        if (!found) {
          tmp.push(result)
        }
        this.taskList = []
        this.taskList = [...tmp]
      }

      this.dialogItem = null
    },

    deleteRecord: function(item) {
      console.log(item)
    },
    formatDate: function(date) {
      date = date.split('-')
      return `${date[2]}.${date[1]}.${date[0]}`
    }
  },
  data: () => ({
    taskList: [],
    showComplete: false,
    showIncomplete: true,
    sortMethod: ["Сначала выполненные", "Сначала не выполненные"],
    dialogItem: null,
    tableHeaders: [
      {
        text: "Заголовок",
        value: "title",
      },
      {
        text: "Статус",
        value: "completed",
      },
      {
        text: "Крайний срок",
        value: "deadline",
      },
      {
        text: "Осталось времени",
        value: "timeleft",
      },
      {
        text: "Важность",
        value: "importance",
      },
      {
        text: "",
        value: "details",
        sortable: false
      },
      {
        text: "",
        value: "complete",
        sortable: false
      },
      {
        text:"",
        value: "delete",
        sortable: false
      }
    ],
  }),
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
