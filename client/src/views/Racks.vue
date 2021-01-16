<template>
  <container fluid >
    <div style="text-align: left;" class= "display-2 font-weight-thick">Racks</div>
    <v-row
    >
      <v-col
        cols="12"
        md="12"
      >
      </v-col>
    </v-row>
    <v-row
    class="grey lighten-5"
    >
      <v-col
        cols="12"
        md="4"
      >
      <v-card
  class="mx-auto text-center"
  outlined
  >
        <v-list flat>
          <v-subheader >Rack info</v-subheader>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
            v-for="(item, i) in allItems"
            :key="i"
          >
          <v-list-item-content>
            <v-list-item-title>{{item.text}}</v-list-item-title>
          </v-list-item-content>
            <v-spacer></v-spacer>
            <v-list-item-content>
              <v-list-item-subtitle>
          {{item.value}}
        </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>
      </v-col>
      <v-col
        cols="12"
        md="8"
      >
      <v-card height="353px">
        test
      </v-card>
      </v-col>
    </v-row>
  </container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import firebase from 'firebase'
export default {
  name: 'racks',
  data () {
    return {
      email: '',
      password: '',
      load: false,
      snackbar: false,
      item: 1,
      items: [
        { text: 'Site', value: 'Kverneland' },
        { text: 'Site Location', value: 'Rig_Ready' },
        { text: 'Rack ID', value: '01A' },
        { text: 'Item Number', value: 'OWS278DP.01' },
        { text: 'Description', value: 'N/A' },
        { text: 'Maxrowcount', value: '20' }
      ]
    }
  },
  methods: {
    clearFields (err) {
      this.password = ''
      this.load = false
      this.snackbar = true
      this.text = 'Oops.. ' + err.message
    },
    ...mapActions(['fetchEmail', 'fetchUsername']),
    login: function () {
      this.load = true
      firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
        (user) => {
          console.log('veve')
          this.fetchEmail()
          this.fetchUsername({ usrname: this.email })
          this.$router.replace('home')
        },
        (err) => {
          this.clearFields(err)
        }
      )
    }
  },
  computed: {
    ...mapGetters([
      'getEmail'
    ]),
    allItems () {
      return this.items
    }
  }
}
</script>

<style lang="css" scoped>

</style>
