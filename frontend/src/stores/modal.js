//  Import defineStore from pinia it will help to create  a store
import { defineStore } from 'pinia'

export default defineStore('modal', {

  state: () => ({
    isOpen: false
  }),
  getters:{
    hiddenClass(state){
      return !state.isOpen ? "btn-close" : ""
    }
  }
})
