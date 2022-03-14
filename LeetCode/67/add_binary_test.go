import "testing"

func TestMain(t *testing.T) {
	data := []struct {
		input  [2]string
		output string
	}{
		{[2]string{"11", "1"}, "100"},
		{[2]string{"1", "11"}, "100"},
		{[2]string{"0", "0"}, "0"},
		{[2]string{"1111", "1111"}, "11110"},
		{[2]string{"101111", "10"}, "110001"},
		{[2]string{"100", "110010"}, "110110"},
	}

	for i, testCase := range data {
		got := addBinary(testCase.input[0], testCase.input[1])
		want := testCase.output

		if got != want {
			t.Errorf("For input index %d - testCase.input %q, %q, got %q, want %q", i, testCase.input[0], testCase.input[1], got, want)
		}
	}
}
