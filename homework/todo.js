class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }

  class SLL {
    constructor() {
      this.head = null;
    }
    addFront(value) {
      var newNode = new Node(value);
      newNode.next = this.head;
      this.head = newNode;
      return this;
    }
    removeFront() {
        if(this.head.next) {
            this.head = this.head.next;
            return this;
        }
        else {
            return null;
        }
    }
    front() {
        if(this.head.value) {
            console.log(this.head.value)
            return this.head.value;
        }
        else{
            return null;
        }
    }
    contains(value) {
        if(value) {
            return true;
        }
        else {
            return false;
        }
    }
    length() {
        var current = this.head;
        var count = 0;
        while(current !== null) {
            current = current.next;
            count ++;
        }
        return count
    }
  }

  var first_node = new Node('Andrew')
  var second_node = new Node('Anthony')
  var third_node = new Node('Anton')
  var fourth_node = new Node('Lewis')

  var this_sll = new SLL();
  this_sll.addFront('Andrew').addFront('Anthony').addFront('Anton').addFront('Lewis')
  console.log(this_sll)
  this_sll.removeFront()
  this_sll.front()
  console.log(this_sll.contains('Andrew'))
  console.log(this_sll.length())


