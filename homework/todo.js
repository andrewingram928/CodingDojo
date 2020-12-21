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
        var current = this.head;
        while(current !== null)
            if(current.value == value) {
                return true;
            }
            else {
                current = current.next;
            }
        return false
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
    display() {
        var current = this.head;
        while(current !== null) {
            console.log(`Current nodes value is ${current.value}`)
            current = current.next;
        }
    }
    max() {
        var current = this.head;
        var max = 0;
        while(current !== null) {
            if(current.value > max) {
                max = current.value;
                console.log(`----The max value in the list is NOW ${max}`)
            }
            current = current.next;
        }
        console.log(`!!!The max value in the list is ${max}!!!`)
    }
    min() {
        var current = this.head;
        var min = current.value;
        while(current !== null) {
            if(current.value < min) {
                min = current.value;
                console.log(`--------The min value in the list is NOW ${min}`)
            }
            current = current.next;
        }
        console.log(`!!!!!The min value in the list is ${min}!!!!!`)
  }
  avg() {
    var current = this.head;
    var sum = 0;
    var count = 0;
    while(current !== null) {
        sum = current.value + sum;
        count ++;
        current = current.next;
    }
    sum = sum / count;
    console.log(sum)
  }
}
var first_node = new Node(8);
var second_node = new Node(10);
var third_node = new Node(15);
var fourth_node = new Node(100);

var this_sll = new SLL();
this_sll.addFront(100).addFront(5).addFront(-2).addFront(50).addFront(800).addFront(5).addFront(10).addFront(6)
console.log(this_sll)
this_sll.removeFront()
this_sll.front()
console.log(this_sll.contains(100))
console.log(this_sll.length())
this_sll.display()
this_sll.max()
this_sll.min()
this_sll.avg()
