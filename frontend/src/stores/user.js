//  Import defineStore from pinia it will help to create  a store
import { defineStore } from 'pinia'

export default defineStore('user', {

  state: () => ({
    userLoggedIn: true
  }),
 
})
