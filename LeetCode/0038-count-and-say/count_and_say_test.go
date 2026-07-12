package countandsay

import (
	"testing"
)

// TestHelloName calls greetings.Hello with a name, checking
// for a valid return value.
func TestCountAndSay(t *testing.T) {
	input := 1
	want := "1"
	actual := CountAndSay(input)
	if actual != want {
		t.Fatalf(`CountAndSay(%d) = %s, expected %v`, input, actual, want)
	}

	input = 2
	want = "11"
	actual = CountAndSay(input)
	if actual != want {
		t.Fatalf(`CountAndSay(%d) = %s, expected %v`, input, actual, want)
	}

	input = 3
	want = "21"
	actual = CountAndSay(input)
	if actual != want {
		t.Fatalf(`CountAndSay(%d) = %s, expected %v`, input, actual, want)
	}

	input = 4
	want = "1211"
	actual = CountAndSay(input)
	if actual != want {
		t.Fatalf(`CountAndSay(%d) = %s, expected %v`, input, actual, want)
	}

	input = 5
	want = "111221"
	actual = CountAndSay(input)
	if actual != want {
		t.Fatalf(`CountAndSay(%d) = %s, expected %v`, input, actual, want)
	}

	input = 6
	want = "312211"
	actual = CountAndSay(input)
	if actual != want {
		t.Fatalf(`CountAndSay(%d) = %s, expected %v`, input, actual, want)
	}

}

// TestHelloEmpty calls greetings.Hello with an empty string,
// checking for an error.
//func TestHelloEmpty(t *testing.T) {
//	msg, err := Hello("")
//	if msg != "" || err == nil {
//		t.Fatalf(`Hello("") = %q, %v, want "", error`, msg, err)
//	}
//}
