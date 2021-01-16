<template>
  <v-app id="inspire">
    <v-snackbar
    v-model="snackbar"
    color='red'
    top
  >
    {{ text }}
    <v-btn
      color="white"
      text
      @click="snackbar = false"
    >
      Close
    </v-btn>
  </v-snackbar>
    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-12"
            tile
            >
              <v-toolbar
                color="white"
                dark
                flat
              >
              <v-spacer></v-spacer>
              <v-img
              contain
              class="white--text align-end"
              height="50px"
              width="70px"
              :src="image"
              ></v-img>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Login"
                    name="login"
                    prepend-icon="person"
                    type="text"
                    v-model="email"
                    :loading="load"
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    label="Password"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                    v-model="password"
                    :loading="load"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn dark color="#204060"
                  @click='login'
                >Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import firebase from 'firebase'
import image from '../assets/picture.png'
export default {
  name: 'login',
  data () {
    return {
      email: '',
      password: '',
      load: false,
      snackbar: false,
      text: '',
      image: image
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
          this.fetchEmail()
          this.fetchUsername({ usrname: this.email })
          console.log(this.getAssetlist)
        },
        (err) => {
          this.clearFields(err)
        }
      )
    }
  },
  computed: {
    ...mapGetters([
      'getEmail','getAssetlist'
    ])
  }
}
</script>

<style lang="css" scoped>

</style>
