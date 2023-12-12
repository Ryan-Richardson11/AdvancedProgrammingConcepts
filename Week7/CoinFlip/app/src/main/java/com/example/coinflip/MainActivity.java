package com.example.coinflip;

import androidx.appcompat.app.AppCompatActivity;
import android.widget.TextView;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import java.util.Random;

public class MainActivity extends AppCompatActivity {
    private TextView resultText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        resultText = findViewById(R.id.resultTextView);

        Button flipButton = findViewById(R.id.flipButton);

        flipButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Call the flipCoin method and update the TextView with the result
                String coinResult = flipCoin();
                resultText.setText(coinResult);
            }
        });
    }


    String flipCoin() {
        Random random = new Random();
        boolean flipResult = random.nextBoolean();
        if (flipResult == true) {
            return "Heads";
        } else {
            return "Tails";
        }
    }

}