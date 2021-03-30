<template>
  <v-dialog persistent v-model="dialog" max-width="50%">
    <v-card>
      <v-card-title class="headline">
        <v-text-field
          v-model="title"
          outlined
          :readonly="!edit"
          label="Заголовок"
        ></v-text-field>
      </v-card-title>

      <v-card-text>
        <div class="d-flex justify-space-between">
          <div class="d-inline-block" style="width: 25%">
            <v-menu
              v-model="showDatePicker"
              :close-on-content-click="true"
              :nudge-right="40"
              transition="scale-transition"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="deadline"
                  label="Дедлайн"
                  append-icon="mdi-calendar"
                  outlined
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                :readonly="!edit"
                v-model="deadline"
                @input="showDatePicker = false"
              ></v-date-picker>
            </v-menu>
          </div>

          <div class="d-inline-block">
            <v-text-field
              outlined
              readonly
              label=""
              :value="calcRemainingTime(deadline)"
            ></v-text-field>
          </div>

          <div class="d-inline-block" style="max-width: 25%">
            <v-select
              outlined
              label="Важность"
              :items="['H', 'M', 'L']"
              v-model="importance"
              :readonly="!edit"
            >
            </v-select>
          </div>
        </div>

        <v-textarea
          outlined
          :readonly="!edit"
          label="Описание"
          v-model="description"
        ></v-textarea>
      </v-card-text>

      <v-card-actions>
        <v-switch v-model="edit" label="Редактировать"></v-switch>
        <v-switch v-model="completed" label="Завершена"></v-switch>
        <v-spacer></v-spacer>

        <v-btn color="primary" text @click="$emit('return', true)"> закрыть </v-btn>
        <v-btn color="primary" text @click="send"> Применить </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "TaskDetail",
  props: ["baseUrl", "token", "item"],
  mounted: function () {
    this.getTaskDetail();
  },
  methods: {
    getTaskDetail: function () {

      if (this.item.id == undefined) {
        this.edit = true
        this.isNewTask = true
        return
      }
      
      let this_ = this;
      this.axios
        .get(`${this.baseUrl}task-detail/${this.item.id}`, {
          headers: {
            Authorization: `Token ${this.token}`,
          },
        })
        .then(function (response) {
          this_.taskDetail = response.data;
          this_.title = response.data.title;
          this_.description = response.data.description;
          this_.importance = response.data.importance;
          this_.deadline = response.data.deadline;
          this_.completed = response.data.completed;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    send: function () {
      let tmp = this.taskDetail;
      if (
        tmp.title != this.title ||
        tmp.description != this.description ||
        tmp.importance != this.importance ||
        tmp.deadline != this.deadline ||
        tmp.completed != this.completed
      ) {
        let newObj = {
          title: this.title,
          description: this.description,
          importance: this.importance,
          deadline: this.deadline,
          completed: this.completed,
        };
        let this_ = this;


        let url = this.baseUrl
        
        if (!this.isNewTask) {
          newObj.id = this.taskDetail.id
          url += `task-update/${this.item.id}/`
        } else {
          url += 'task-create/' 
        }

        console.log(newObj)

        this.axios({
          method: this.isNewTask ? 'post' : 'patch',
          url: url,
          data: newObj,
          headers: {
            Authorization: `Token ${this.token}`,
          },
        })
          .then(function (response) {
            console.log(response);
            console.log(response.status)
            if (response.status == 200 || response.status == 201) {
              this_.$emit("return", newObj);
              newObj.id = response.data.id
            }
          })
          .catch(function (error) {
            console.error(error);
            alert('Изменения не были внесены')
          });
      } else {
        this.$emit("return", true);
      }
    },
    calcRemainingTime: function (deadline) {
      if (!deadline) return ''
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
    clearFields: function() {
      /*this.taskDetail = {},
      this.dialog = true,
      this.edit = false,
      this.title = null,
      this.description = null,
      this.importance = null,
      this.deadline = null,
      this.complete = false,
      this.showDatePicker = false,
      this.importanceList = ["*****", "***", "*"],
      this.isNewTask = false*/


      //this.$emit('return', true)
        this.$emit('return', true)

      }
  },
  watch: {
    edit: function (newValue) {
      if (newValue == false) {
        this.title = this.taskDetail.title;
        this.description = this.taskDetail.description;
        this.importance = this.taskDetail.importance;
        this.deadline = this.taskDetail.deadline;
        this.completed = this.taskDetail.completed;
      }
    },
  },
  data: () => ({
    taskDetail: {},
    dialog: true,
    edit: false,
    title: null,
    description: null,
    importance: null,
    deadline: null,
    completed: false,
    showDatePicker: false,
    importanceList: ["*****", "***", "*"],
    isNewTask: false
  }),
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
